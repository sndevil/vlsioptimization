module F3 (a , VV1V , d , VV2V , VV3V); 
input a , VV1V , d , VV2V;
output VV3V;
wire WW2W0W , WW2W1W , WW2W2W;

not f0 (WW2W0W , a);
and f1 (WW2W1W , VV1V , WW2W0W);
or f2 (WW2W2W , WW2W1W , d);
or f3 (VV3V , WW2W2W , VV2V);
endmodule