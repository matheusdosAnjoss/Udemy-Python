from log import LogPrintMixin, LogFileMixin

l = LogPrintMixin()
l.log_error("qualquer coisa")
l.log_success("qualquer coisa")
    

lf = LogFileMixin()
lf.log_error("qualquer coisa")
lf.log_success("que legal")
    