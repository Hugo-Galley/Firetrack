
########################################################################
## IMPORTS
########################################################################
import sys
import os
from PySide2 import QtCore, QtGui

########################################################################
# IMPORT DU Fichier interface
from ui_interface import *
########################################################################


########################################################################
## Classe MAIN WINDOW
########################################################################
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #######################################################################
        ## # Retire la base Windows
        ########################################################################    
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 

        #######################################################################
        ## # Rendre l'arrièe plan transparent
        ########################################################################  
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
      
        #######################################################################
        ## # Effet d'ombre
        ########################################################################  
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 550))
        
        #######################################################################
        ## # Applique l'ombre sur le widget central
        ########################################################################  
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        #######################################################################
        # Icône de la fenêtre
        # P.S- ça ne va pas s'afficher. ça fait parti de la barre de fenêtre Windows
        #######################################################################
        self.setWindowIcon(QtGui.QIcon(":/icons/icons/headphones.svg"))
        # Nom de la fenêtre
        self.setWindowTitle("Despacito UI")

        #################################################################################
        # Poignée de taille de fenêtre Windows
        #################################################################################
        QSizeGrip(self.ui.size_grip)

        #######################################################################
        #Minimize la fenêtre
        self.ui.minimize_window_button.clicked.connect(lambda: self.showMinimized())
        #######################################################################
        #Ferme la fenêtre
        self.ui.close_window_button.clicked.connect(lambda: self.close())
        self.ui.exit_button.clicked.connect(lambda: self.close())


        #######################################################################
        #Rétablis/Maximize la fenêtre
        self.ui.restore_window_button.clicked.connect(lambda: self.restore_or_maximize_window())


        # ###############################################
        # Fonction de déplacement lors de glissement de souris
        # ###############################################
        def moveWindow(e):
            # Détecte si la fenêtre est de taille normale
            # ###############################################  
            if self.isMaximized() == False: #Not maximized
                # Déplace la fenêtre que si elle est de taille normale 
                # ###############################################
                #SI le bouton gauche de la souris est appuyé
                if e.buttons() == Qt.LeftButton:  
                    #Déplacer la fenêtre 
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        #######################################################################

        #######################################################################
        #  Crée une évènement click/déplacement de souris/drag le haut de la fenêtre pour la déplacer
        #######################################################################
        self.ui.header_frame.mouseMoveEvent = moveWindow
        #######################################################################


        #######################################################################
        #Bouton d'ectivation du menu de gauche
        self.ui.open_close_side_bar_btn.clicked.connect(lambda: self.slideLeftMenu())


        self.show()




    ########################################################################
    # Slide menu non fonctionnel###
    ########################################################################
    def slideLeftMenu(self):
        # Prend la largeur actuelle du menu
        width = self.ui.slide_menu_container.width()

        # Si minimisé
        if width == 0:
            # Etendre le menu
            newWidth = 200
            self.ui.open_close_side_bar_btn.setIcon(QtGui.QIcon(u":/icons/icons/chevron-left.svg"))
        # Si maximisé
        else:
            # Restore le menu
            newWidth = 0
            self.ui.open_close_side_bar_btn.setIcon(QtGui.QIcon(u":/icons/icons/align-left.svg"))

        # Animation de transition
        self.animation = QPropertyAnimation(self.ui.slide_menu_container, b"maximumWidth")#Anime la largeur minimum du menu
        self.animation.setDuration(250)
        self.animation.setStartValue(width)#Valeur de base de largeur du menu
        self.animation.setEndValue(newWidth)#Valeur finale de laergeur du menu
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
    #######################################################################





    #######################################################################
    # Ajoute l'évé=ènement de souris àla fenêtre
    #######################################################################
    def mousePressEvent(self, event):
        # ###############################################
        # Prends la postion actuelle de la souris
        self.clickPosition = event.globalPos()
        # On va utiliser cette valeur pour déplacer la fenêtre
    #######################################################################
    #######################################################################



    #######################################################################
    # Met à jour l'incône du bouton quannd on maximize ou minimise la fenêtre
    #######################################################################
    def restore_or_maximize_window(self):
        # Si la fenêtre est maximisée
        if self.isMaximized():
            self.showNormal()
            # Change l'icône
            self.ui.restore_window_button.setIcon(QtGui.QIcon(u":/icons/icons/maximize-2.svg"))
        else:
            self.showMaximized()
            # Change l'icône
            self.ui.restore_window_button.setIcon(QtGui.QIcon(u":/icons/icons/minimize-2.svg"))

########################################################################
## EXECUTE L'APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
########################################################################
## FIN===>
########################################################################  
