import cx_Freeze

executables = [cx_Freeze.Executable("coronagame.py")]

cx_Freeze.setup(
    name="Corona Game",
    options={"build_exe":{"packages":["pygame"],
                          "include_files":["data","data/virus","data/virus/attacking","data/virus/moving","data/usa","data/usa/appearing","data/syringe","data/right_bar","data/player","data/player/back","data/player/forward","data/player/left","data/player/right","data/italy","data/italy/appearing","data/iran","data/iran/appearing","data/house","data/health_bar_full","data/health_bar_empty","data/fence","data/dummy","data/DNA_yellow","data/DNA_yellow/unlocking","data/DNA_white","data/DNA_white/unlocking","data/DNA_red","data/DNA_red/unlocking","data/DNA_purple","data/DNA_purple/unlocking","data/DNA_pink","data/DNA_pink/unlocking","data/DNA_orange","data/DNA_orange/unlocking","data/DNA_green","data/DNA_green/unlocking","data/DNA_brown","data/DNA_brown/unlocking","data/DNA_blue","data/DNA_blue/unlocking","data/DNA_black","data/DNA_black/unlocking","data/China","data/China/appearing","data/car"]}},
    executables=executables
    )
