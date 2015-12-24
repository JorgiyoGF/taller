#! /usr/bin/python
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from gi.repository import Gtk

from conexion import bd

import clientes

import factura

class main:

    def __init__(self):

#declaracion de widgets
        b = Gtk.Builder()
        b.add_from_file("taller.glade")
        self.ventanaPrincipal = b.get_object("ventanaPrincipal")
        self.ventanaNeocli = b.get_object("ventanaNeocli")
        self.btnSalircli = b.get_object("btnSalircli")
        self.btnNeocli = b.get_object("btnNeocli")
        self.btnGrabcli = b.get_object("btnGrabcli")
        self.btnSalir = b.get_object("btnSalir")
        self.listCliente = b.get_object("listCliente")
        self.dnicli = b.get_object("entDni")
        self.apelcli = b.get_object("entApel")
        self.nomcli = b.get_object("entNom")
        self.dircli = b.get_object("entDir")
        self.loccli = b.get_object("entLoc")
        self.provcli = b.get_object("entProv")
        self.cpcli = b.get_object("entCp")
        self.movcli = b.get_object("entMov")
        self.telcli = b.get_object("entTel")
        self.mailcli = b.get_object("entMail")
        self.sicli = b.get_object("rtbSi")
        self.nocli = b.get_object("rtbNo")
        self.entMatrifac = b.get_object("entMatri")
        self.entModelfac = b.get_object("entModel")
        self.entFechafac = b.get_object("entFecha")
        self.entMarcafac = b.get_object("entMarca")
        self.lbldnifac = b.get_object("lbldnifac")
        self.lblidfac = b.get_object("lblidfac")
        self.avisodni = b.get_object("dlgAvis")
        self.btnAceptar = b.get_object("btnAceptar")
        self.listCliente = b.get_object("listCiente")
        self.trewCliente = b.get_object("trwCliente")
        self.listFactura = b.get_object("listFactura")
        self.trewFactura = b.get_object("trewFactura")        
        self.btnBorrarcli = b.get_object("btnBorrarcli")
        self.ventanaTaller = b.get_object("ventanaTaller")
        self.btnGrabarfac = b.get_object("btnGrabarfac")
        self.ventanaPrincipal.show()
        clientes.mostrar(self.listCliente, self.trewCliente)
        

        dic = {"on_btnNeocli_clicked": self.on_btnNeocli_clicked,
            "on_btnSalir_clicked": self.on_btnSalir_clicked,
            "on_btnSalircli_clicked": self.on_btnSalircli_clicked,
            "on_btnGrabcli_clicked": self.on_btnGrabcli_clicked,
            "on_ventanaPrincipal_destroy": self.on_ventanaPrincipal_destroy,
            "on_ventanaNeocli_delete_event": self.on_ventanaNeocli_delete_event,
            "on_entDni_focus_out_event": self.on_entDni_focus_out_event,
            "on_btnAceptar_clicked": self.on_btnAceptar_clicked,
            "on_rbtNo_toggled": self.on_rbtNo_toggled,
            "on_btnBorrarcli_clicked": self.on_btnBorrarcli_clicked,
            "on_trwCliente_cursor_changed": self.on_trwCliente_cursor_changed,
            "on_trewFactura_cursor_changed": self.on_trewFactura_cursor_changed,
            "on_btnTaller_clicked": self.on_btnTaller_clicked,
            "on_btnSalirtaller_clicked": self.on_btnSalirtaller_clicked,
            "on_btnGrabarfac_clicked": self.on_btnGrabarfac_clicked,
            "on_ventanaTaller_destroy": self.on_ventanaTaller_destroy
            }

        b.connect_signals(dic)

#declaracion y codificacion de funciones
    def on_btnTaller_clicked(self,  widget):
        self.lbldnifac.set_text(self.data)
        factura.mostrar(self.listFactura, self.trewFactura)
        self.ventanaTaller.show()
       
    def on_ventanaTaller_destroy(self, widget):
        self.ventanaTaller.hide()
        return True
    
    def on_btnSalirtaller_clicked(self, widget):
        self.ventanaTaller.hide()
        return True
    
    def on_btnGrabarfac_clicked(self, widget):
        self.dnifac = self.data
        self.matrifac = self.entMatrifac.get_text()
        self.marcafac = self.entMarcafac.get_text()
        self.modelfac = self.entModelfac.get_text()
        self.fechafac = self.entFechafac.get_text()
        if factura.Grabarfac(self.dnifac, self.matrifac, self.marcafac, self.modelfac, self.fechafac) == False:
            self.aviso.show()
        factura.limpiarfac(self.lbldnifac, self.entMatrifac, self.entMarcafac, self.entModelfac, self.entFechafac, self.lblidfac)
        factura.mostrar(self.listFactura, self.trewFactura)
    
    def on_trewFactura_cursor_changed(self, widget):
        print "hola"

    
    def on_trwCliente_cursor_changed(self, widget, Data=None):
        self.seleccion = self.trewCliente.get_selection()
        model, iter = self.seleccion.get_selected()
        self.data = model[iter][0]
        self.data = str(self.data)
                            
    def on_btnBorrarcli_clicked(self, widget):
        clientes.Borrarcli(self.data)
        clientes.mostrar(self.listCliente, self.trewCliente)  
        
    def on_btnNeocli_clicked(self, widget, data=None):
        self.ventanaNeocli.show()
        self.pub = "no"

    def on_btnSalir_clicked(self, widget):
        Gtk.main_quit()

    def on_ventanaPrincipal_destroy(self, widget):
        Gtk.main_quit()

    def on_ventanaNeocli_delete_event(self, widget, data=None):
        self.ventanaNeocli.hide()
        return True

    def on_btnAceptar_clicked(self, widget):
        self.avisodni.hide()
        return True

    def on_entDni_focus_out_event(self, widget, Data=None):
        self.dni = self.dnicli.get_text()
        self.dni = self.dni.upper()
        self.dnicli.set_text(self.dni)
        if (clientes.validoDNI(self.dni) is False and self.dni != ""):
            self.avisodni.show()
            self.dnicli.set_text("")

    def on_btnSalircli_clicked(self, widget, Data=None):
        self.ventanaNeocli.hide()
        return True

    def on_rbtNo_toggled(self, widget, Data=None):
        if widget.get_active():
            self.pub = "no"
        else:
            self.pub = "si"
             
    def on_btnGrabcli_clicked(self, widget):
        self.dni = self.dnicli.get_text()
        self.apel = self.apelcli.get_text()
        self.nom = self.nomcli.get_text()
        self.dir = self.dircli.get_text()
        self.loc = self.loccli.get_text()
        self.prov = self.provcli.get_text()
        self.cp = self.cpcli.get_text()
        self.mov = self.movcli.get_text()
        self.tel = self.telcli.get_text()
        self.mail = self.mailcli.get_text()
              
        if clientes.Grabarcli(self.dni, self.apel, self.nom, self.dir, self.loc, self.prov, self.cp, self.mov, self.tel, self.mail, self.pub) == False:
            self.avisodni.show()
            
        clientes.limpiarcli(self.dnicli, self.apelcli, self.nomcli, self.dircli, self.loccli, self.provcli, self.cpcli, self.movcli, self.telcli, self.mailcli)
        clientes.mostrar(self.listCliente, self.trewCliente)

if __name__ == "__main__":
    main = main()
    Gtk.main()