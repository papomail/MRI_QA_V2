script_path=getDirectory("current");
//home_path=getDirectory("home");


// RUN SNR:
runMacro(script_path + "SNR.ijm") ;

// RUN SIGNAL UNIFORMITY:
 //runMacro(script_path + "SIGNAL_UNIFORMITY.ijm") ;
runMacro(script_path + "SIGNAL_UNIFORMITY_NOPLOTS.ijm") ;

// RUN GEOMETRIC_LINEARITY:
runMacro(script_path + "GEOMETRIC_LINEARITY.ijm");


// RUN SLICE WIDTH:
runMacro(script_path + "SLICE_WIDTH.ijm");


// RUN GHOSTING:
runMacro(script_path + "GHOSTING.ijm");


// RUN SLICE_POS:
// NOT READY!!! 
runMacro(script_path + "SLICE_POSITION2.ijm");



// close("*");

print("");
print("");
print("");
print("Done! Closing FIJI now... ");

run("Quit");
