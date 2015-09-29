module F3 (a , c , VV3V); 
input a , c;
output VV3V;
wire WW2W0W , WW2W1W;

not f0 (WW2W0W , a);
not f1 (WW2W1W , c);
xor f2 (VV3V , WW2W0W , WW2W1W);
endmodule