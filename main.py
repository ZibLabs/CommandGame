print("Hello welcome to Command Game")
print("type help for get started with basic commands")
MONEY = 1002
UsedUpgradeSlots = 0
MaxUpgradeSlots = 3
RAM = 1
RAMUpgrades = 0
CPUUpgrades = 0
CPU = 2
WIFIUpgrades = 0
WIFI = 1
MOTHERBOARDUpgrades = 0
MOTHERBOARD = 1
CRACKER = 0
CRACKERv1ISLOCKED = True
print()
while True:
  USERinput = input()
  if USERinput == "help":
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("help - shows this message")
    print("tut - starts or restarts tutorial")
    print("credits - shows credits")
    print("store - opens the store page")
    print("upgrades - opens the upgrades page")
    print("skills - opens the skill tree")
    print("command - opens the command line")
    print("TBI - to be implimented")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
  if USERinput == "tut":
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("tutorial yet to be imlimented figure it out I guess")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  if USERinput == "credits":
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Game made by: GZ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
  if USERinput == "tbi":
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("I told you it was To Be Implimented")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
  if USERinput == "store":
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Welcome to the Computer Store")
    print("You have", MONEY, "UNITS")
    print("UPGRADE SLOTS:", UsedUpgradeSlots, "Out of", MaxUpgradeSlots)
    print("MORE RAM - 50 UNITS - HAVE ONE MORE COMMAND RUNNING AT ONCE - TYPE RAM")
    print("BETTER CPU - 25 UNITS - COMPUTING COMMANDS RUN FASTER - TYPE CPU")
    print("BETTER WIFI CHIP     - 25 UNITS - NETWORK COMMANDS RUN FASTER - TYPE WIFI")
    print("BETTER MOTHERBOARD - 100 UNITS - MORE UPGRADE SLOTS - TYPE MOTHERBOARD")
    print("CRACKING SOFTWARE - 50 UNITS - ALLOWS YOU TO CRACK SIMPLE NETWORK PASSWORDS AUTOMATICALLY - TYPE CRACKER")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    storeinput = input()
    if storeinput == "RAM":
      if MONEY >= 50:
        if UsedUpgradeSlots < MaxUpgradeSlots:
          MONEY = MONEY - 50
          RAMUpgrades = RAMUpgrades + 1
          RAM = RAM * 2
          print("You have bought RAM")
          print("You now have", MONEY, "UNITS")
          print("You now have", RAM, "GBs OF RAM")
          print("You now have", RAMUpgrades, "RAM Upgrades")
          UsedUpgradeSlots = RAMUpgrades + CPUUpgrades + WIFIUpgrades
          print("You have", UsedUpgradeSlots, "out of", MaxUpgradeSlots,
                "Upgrade Slots")
        else:
          print("YOU HAVE NO MORE UPGRADE SLOTS")
      else:
        print("NOT ENOUGH UNITS")
    if storeinput == "CPU":
      print("you bought a CPU upgrade")
      if MONEY >= 25:
        if UsedUpgradeSlots < MaxUpgradeSlots:
          MONEY = MONEY - 25
          UsedUpgradeSlots = UsedUpgradeSlots + 1
          CPUUpgrades = CPUUpgrades + 1
          CPU = CPU + 2
          print("You now have", MONEY, "UNITS")
          print("You now have", CPU, "CPU Cores")
          print("You now have", CPUUpgrades, "CPU Upgrades")
          print("You now have", UsedUpgradeSlots, "out of", MaxUpgradeSlots, "Upgrade Slots")
        else:
          print("YOU HAVE NO MORE UPGRADE SLOTS")
      else:
        print("NOT ENOUGH UNITS")
    if storeinput == "WIFI":
      if MONEY >= 25:
        if UsedUpgradeSlots < MaxUpgradeSlots:
          print("you bought a WIFI upgrade")
          MONEY = MONEY - 25
          UsedUpgradeSlots = UsedUpgradeSlots + 1
          WIFIUpgrades = WIFIUpgrades + 1
          WIFI = WIFI + 1
          print("You now have", MONEY, "UNITS")
          print("You now have a V", WIFI, "WIFI CHIP")
        else:
          print("YOU HAVE NO MORE UPGRADE SLOTS")
      else:
        print("NOT ENOUGH UNITS")
    if storeinput == "MOTHERBOARD":
      if MONEY >= 100:
        print("you bought a MOTHERBOARD upgrade")
        MONEY = MONEY - 100
        MOTHERBOARDUpgrades = MOTHERBOARDUpgrades + 1
        MOTHERBOARD = MOTHERBOARD + 1
        MaxUpgradeSlots = MOTHERBOARD + 3
        print("You now have", MONEY, "UNITS")
        print("You now have a V", MOTHERBOARD, "MOTHERBOARD")

    if storeinput == "CRACKER":
      if MONEY >= 50:
        if CRACKERv1ISLOCKED == True:
          print("you bought a CRACKER upgrade")
          MONEY = MONEY - 50
          CRACKER = CRACKER + 1
          CRACKERv1ISLOCKED = False
          print("You now have", MONEY, "UNITS")
         print("You now have NETWORK CRACKING SOFTWARE V1")
      else:
        print("NOT ENOUGH UNITS")
    continue
  if USERinput == "upgrades":
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("These are your computers current upgrades.")
    print("RAM:", RAM, "GB.", "- UPGRADES DONE TO RAM:", RAMUpgrades)
    print("CPUs:", CPU," CPU Cores" , "- UPGRADES DONE TO CPU:", CPUUpgrades)
    print("WIFI CHIP: V", WIFI, "- UPGRADES DONE TO WIFI:", WIFIUpgrades)
    print("MOTHBOARD: V", MOTHERBOARD, "- UPGRADES DONE TO MOTHERBOARD:",
          MOTHERBOARDUpgrades)
    print("TO SELL UPGRADES TYPE SELL AND THEN UPGRADE YOU WANT TO SELL")
    print("UPGRADE SLOTS:", UsedUpgradeSlots, "Out of", MaxUpgradeSlots)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    exit
