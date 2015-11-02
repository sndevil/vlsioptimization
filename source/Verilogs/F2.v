module F2 (VV1V , c , d , VV2V); 
input VV1V , c , d;
output VV2V;
wire WW1W0W;

and f0 (WW1W0W , VV1V , c);
xor f1 (VV2V , WW1W0W , d);
endmodule