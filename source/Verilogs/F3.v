module F3 (VV2V , t , r , VV3V); 
input VV2V , t , r;
output VV3V;
wire WW2W0W , WW2W1W;

not f0 (WW2W0W , VV2V);
xor f1 (WW2W1W , t , r);
and f2 (VV3V , WW2W1W , WW2W0W);
endmodule