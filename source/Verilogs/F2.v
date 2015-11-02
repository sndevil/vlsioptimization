module F2 (c , VV1V , d , VV2V); 
input c , VV1V , d;
output VV2V;
wire WW1W0W , WW1W1W;

not f0 (WW1W0W , c);
and f1 (WW1W1W , VV1V , WW1W0W);
xor f2 (VV2V , WW1W1W , d);
endmodule