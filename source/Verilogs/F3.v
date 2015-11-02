module F3 (a , d , c , VV3V); 
input a , d , c;
output VV3V;
wire WW2W0W , WW2W1W;

not f0 (WW2W0W , a);
and f1 (WW2W1W , d , c);
xor f2 (VV3V , WW2W1W , WW2W0W);
endmodule