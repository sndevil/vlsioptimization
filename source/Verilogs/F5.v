module F5 (VV1V , VV3V , VV4V , VV5V); 
input VV1V , VV3V , VV4V;
output VV5V;
wire WW4W0W;

and f0 (WW4W0W , VV1V , VV3V);
xor f1 (VV5V , WW4W0W , VV4V);
endmodule