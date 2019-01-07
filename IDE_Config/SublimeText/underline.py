import sublime
import sublime_plugin


class UnderlineCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        for r in self.view.sel():
            full_line = self.view.full_line(r)
            line = self.view.line(r)
            self.view.insert(edit, full_line.b, '-' * line.size() + '\n')