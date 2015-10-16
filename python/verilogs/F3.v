module F3 (b , c , VV3V); 
input b , c;
output VV3V;
wire WW2W0W , WW2W1W;

not f0 (WW2W0W , b);
not f1 (WW2W1W , c);
and f2 (VV3V , WW2W0W , WW2W1W);
endmodule