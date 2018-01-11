################################################################################
##                                                                            ##
##  Copyright (C) 2011-2015, Armory Technologies, Inc.                        ##
##  Distributed under the GNU Affero General Public License (AGPL v3)         ##
##  See LICENSE-ATI or https://www.gnu.org/licenses/agpl.html                 ##
##                                                                            ##
##  Copyright (C) 2016-2018, goatpig                                          ##
##  Distributed under the MIT license                                         ##
##  See LICENSE-MIT or https://opensource.org/licenses/MIT                    ##
##                                                                            ##
################################################################################
import sys

from ldtp import objectexist
from unittest import TestCase


MAIN_WINDOW = "dlgArmory*dlgMain"

# buttons on left-hand side
BTN_SENDBITCOINS = "btnSendBitcoins"
BTN_RECEIVEBITCOINS = "btnReceiveBitcoins"
BTN_WALLETPROPERTIES = "btnWalletProperties"
BTN_OFFLINETRANSACTIONS = "btnOfflineTransactions"

LEFT_HAND_BUTTONS = [BTN_SENDBITCOINS, BTN_RECEIVEBITCOINS, BTN_WALLETPROPERTIES, BTN_OFFLINETRANSACTIONS,]

# File
MNU_FILE = "mnuFile"

MNU_EXPORTTRANSACTIONS = "mnuExportTransactions"
MNU_SETTINGS = "mnuSettings"
MNU_MINIMIZEARMORY = "mnuMinimizeArmory"
MNU_EXPORTLOGFILE = "mnuExportLogFile"
MNU_QUITARMORY = "mnuQuitArmory"

# User
MNU_USER = "mnuUser"

MNU_STANDARD = "mnuStandard"
MNU_ADVANCED = "mnuAdvanced"
MNU_EXPERT = "mnuExpert"

# Tools
MNU_TOOLS = "mnuTools"

MNU_MESSAGESIGNINGVERIFICATION = "mnuMessageSigning/Verification"
MNU_ECCALCULATOR = "mnuECCalculator"
MNU_BROADCASTRAWTRANSACTION = "mnuBroadcastRawTransaction"

# Addresses
MNU_ADDRESSES = "mnuAddresses"

MNU_VIEWADDRESSBOOK = "mnuViewAddressBook"
MNU_IMPORTPRIVATEKEYADDRESS = "mnuImportPrivateKey/Address"
MNU_SWEEPPRIVATEKEYADDRESS = "mnuSweepPrivateKey/Address"

# Wallets
MNU_WALLETS = "mnuWallets"

MNU_CREATENEWWALLET = "mnuCreateNewWallet"
MNU_IMPORTORRESTOREWALLET = "mnuImportorRestoreWallet"
MNU_FIXDAMAGEDWALLET = "mnuFixDamagedWallet"

# Multisig
MNU_MULTISIG = "mnuMultiSig"

MNU_LOCKBOXMANAGER = "mnuLockboxManager"
MNU_SIMULFUNDCOLLECTMERGE = "mnuSimulfundCollect&Merge"
MNU_SIMULFUNDPROMISSORYNOTE = "mnuSimulfundPromissoryNote"
MNU_SIMULFUNDREVIEWSIGN = "mnuSimulfundReview&Sign"

# Help
MNU_HELP = "mnuHelp"

MNU_ABOUTARMORY = "mnuAboutArmory"
MNU_ARMORYVERSION = "mnuArmoryVersion"
MNU_UPDATESOFTWARE = "mnuUpdateSoftware"
MNU_VERIFYSIGNEDPACKAGE = "mnuVerifySignedPackage"
MNU_TROUBLESHOOTINGARMORY = "mnuTroubleshootingArmory"
MNU_SUBMITBUGREPORT = "mnuSubmitBugReport"
MNU_ARMORYPRIVACYPOLICY = "mnuArmoryPrivacyPolicy"
MNU_CLEARALLUNCONFIRMED = "mnuClearAllUnconfirmed"
MNU_REBUILDANDRESCANDATABASES = "mnuRebuildandRescanDatabases"
MNU_RESCANDATABASES = "mnuRescanDatabases"
MNU_FACTORYRESET = "mnuFactoryReset"

MENU_ITEMS = [MNU_FILE, MNU_EXPORTTRANSACTIONS, MNU_SETTINGS, MNU_MINIMIZEARMORY, MNU_EXPORTLOGFILE, MNU_QUITARMORY, MNU_USER, MNU_STANDARD, MNU_ADVANCED, MNU_EXPERT, MNU_TOOLS, MNU_MESSAGESIGNINGVERIFICATION, MNU_ECCALCULATOR, MNU_BROADCASTRAWTRANSACTION, MNU_ADDRESSES, MNU_VIEWADDRESSBOOK, MNU_IMPORTPRIVATEKEYADDRESS, MNU_SWEEPPRIVATEKEYADDRESS, MNU_WALLETS, MNU_CREATENEWWALLET, MNU_IMPORTORRESTOREWALLET, MNU_FIXDAMAGEDWALLET, MNU_MULTISIG, MNU_LOCKBOXMANAGER, MNU_SIMULFUNDCOLLECTMERGE, MNU_SIMULFUNDPROMISSORYNOTE, MNU_SIMULFUNDREVIEWSIGN, MNU_HELP, MNU_ABOUTARMORY, MNU_ARMORYVERSION, MNU_UPDATESOFTWARE, MNU_VERIFYSIGNEDPACKAGE, MNU_TROUBLESHOOTINGARMORY, MNU_SUBMITBUGREPORT, MNU_ARMORYPRIVACYPOLICY, MNU_CLEARALLUNCONFIRMED, MNU_REBUILDANDRESCANDATABASES, MNU_RESCANDATABASES, MNU_FACTORYRESET,]

# Wallet Action Buttons
BTN_CREATEWALLET = "btnCreateWallet"
BTN_IMPORTORRESTOREWALLET = "btnImportorRestoreWallet"

WALLET_BUTTONS = [BTN_CREATEWALLET, BTN_IMPORTORRESTOREWALLET,]

class GuiTest(TestCase):

    def testLeftHandButtons(self):
        for button in LEFT_HAND_BUTTONS:
            self.assertTrue(objectexist(MAIN_WINDOW, button))

    def testMenuItems(self):
        for item in MENU_ITEMS:
            self.assertTrue(objectexist(MAIN_WINDOW, item))

    def testWalletButtons(self):
        for button in WALLET_BUTTONS:
            self.assertTrue(objectexist(MAIN_WINDOW, button))
