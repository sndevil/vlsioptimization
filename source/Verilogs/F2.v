module F2 (a , VV1V , VV2V); 
input a , VV1V;
output VV2V;
wire WW1W0W;

not f0 (WW1W0W , a);
xor f1 (VV2V , VV1V , WW1W0W);
endmodule