module F3 (d , a , c , VV3V); 
input d , a , c;
output VV3V;
wire WW2W0W , WW2W1W;

not f0 (WW2W0W , d);
or f1 (WW2W1W , a , c);
xor f2 (VV3V , WW2W1W , WW2W0W);
endmodule