from pywingui.windows import *
from pywingui.wtl import *
from pywingui.comctl import *
from pywingui.lib import list
from pywingui.lib import form
from pywingui.lib import splitter
from pywingui.gdi import SolidBrush

column_defs = [('Errors', 100)]

InitCommonControls(ICC_LISTVIEW_CLASSES | ICC_COOL_CLASSES | ICC_USEREX_CLASSES)


class ErrorList(list.List):
    _window_style_ = WS_CHILD | WS_VISIBLE | LVS_REPORT | LVS_SINGLESEL | LVS_EX_AUTOSIZECOLUMNS

    def on_click(self, event):
        nmlv = NMLISTVIEW.from_address(event.lParam)
        self.parent.set_exception_details(nmlv.iItem)
    ntf_handler(NM_CLICK)(on_click)

    def on_size(self, event):
        width = self.clientRect.width
        self.SetRedraw(0)
        self.SetColumnWidth(0, width)
        self.SetRedraw(1)
        event.handled = False
    msg_handler(WM_SIZE)(on_size)


class ErrorDescription(Edit):
    _window_style_ = WS_CHILD | WS_VISIBLE | ES_MULTILINE
    def SetText(self, text):
        if UNICODE:
            txt = create_unicode_buffer(text)
        else:
            txt = create_string_buffer(text)
        self.SendMessage(WM_SETTEXT, 0, txt)


class ErrorForm(form.Form):
    _window_background_ = 0
    _window_title_ = 'Obsanity'

    _form_menu_ = [
        (MF_POPUP, '&File',
            [
                (MF_STRING, '&Save Results', form.ID_SAVE),
                (MF_SEPARATOR,),
                (MF_STRING, '&Exit', form.ID_EXIT)
            ]
        )
    ]

    def OnCreate(self, event):
        self.error_list = ErrorList(parent=self, orExStyle=WS_EX_CLIENTEDGE)
        self.error_list.SetExtendedListViewStyle(0, LVS_EX_FULLROWSELECT | LVS_EX_DOUBLEBUFFER)
        self.error_list.InsertColumns(column_defs)
        self.error_desc = ErrorDescription(parent=self)
        self.error_sb = StatusBar(parent = self)
        self.error_sb.Simple(True)

        error_splitter = splitter.Splitter(parent=self, splitPos=200, orientation=splitter.HORIZONTAL)
        error_splitter.Add(0, self.error_list)
        error_splitter.Add(1, self.error_desc)

        self.controls.Add(form.CTRL_VIEW, error_splitter)
        self.controls.Add(self.error_list)
        self.controls.Add(self.error_desc)
        self.controls.Add(form.CTRL_STATUSBAR, self.error_sb)

    def add_exceptions(self, exc):
        self.exceptions = exc
        self.exc = []
        msg = 'rule {0}: {1}'
        for r, e in exc:
            if len(e):
                for re in e:
                    self.exc.append((r, re))
                    hr = self.error_list.InsertRow(-1, ([msg.format(r, re['type'])]))

    def set_exception_details(self, index):
        r, e = self.exc[index]
        msg = 'Rule: {0}\r\n\r\nException: {1}\r\n\r\nResolution: {2}\r\n\r\nType: {3}'
        self.error_desc.SetText(msg.format(r, e['exception'], e['resolution'], e['type']))

    def on_destroy(self, event):
        self.application.Quit()
    msg_handler(WM_DESTROY)(on_destroy)

    def OnSave(self, event):
        import gist
        self.error_sb.SetText('Creating gist...')
        try:
            url = gist.create_gist(self.exceptions)
        except:
            self.error_sb.SetText('Failed to create gist :-(')
            return

        text_to_clipboard(self, hwnd=0, text=url)
        self.error_sb.SetText('Gist URL saved to clipboard')
        self.error_sb.UpdateWindow()

    cmd_handler(form.ID_SAVE)(OnSave)


def run_gui(exceptions):
    error_form = ErrorForm(rcPos = RECT(0, 0, 800, 600))
    error_form.ShowWindow()
    error_form.add_exceptions(exceptions)

    error_form.application = application = Application()
    application.Run()
