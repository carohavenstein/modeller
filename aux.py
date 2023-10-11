#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  aux.py
#
#  Copyright 2023 John Coppens <john@jcoppens.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#


import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GooCanvas', '2.0')
from gi.repository import Gtk, GooCanvas


def warning(primary, secondary):
    dlg = Gtk.MessageDialog(
                message_type = Gtk.MessageType.WARNING,
                secondary_text = secondary,
                text = primary,
                buttons = Gtk.ButtonsType.CLOSE)
    dlg.run()
    dlg.destroy()


def confirmed(primary, secondary):
    dlg = Gtk.MessageDialog(
                message_type = Gtk.MessageType.WARNING,
                secondary_text = secondary,
                text = primary,
                buttons = Gtk.ButtonsType.OK_CANCEL)
    accepted = dlg.run() == Gtk.ResponseType.OK
    dlg.destroy()
    return accepted


class MainWindow(Gtk.Window):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.connect("destroy", lambda x: Gtk.main_quit())
        self.set_default_size(400, 300)

        wbtn = Gtk.Button(label = 'Test Warning')
        wbtn.connect('clicked', self.on_wbtn_clicked)
        cbtn = Gtk.Button(label = 'Test_confirmation')
        cbtn.connect('clicked', self.on_cbtn_clicked)

        grid = Gtk.Grid()
        grid.attach(wbtn, 0, 0, 1, 1)
        grid.attach(cbtn, 0, 1, 1, 1)
        self.add(grid)
        self.show_all()


    def on_wbtn_clicked(self, btn):
        warning('Aviso', 'No hay nada que decir')


    def on_cbtn_clicked(self, btn):
        if confirmed('Confirmación', 'Acceptar'):
            print('Fue confirmado')
        else:
            print('Fue cancelado')


    def run(self):
        Gtk.main()


def main(args):
    mainwdw = MainWindow()
    mainwdw.run()

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
