module F5 (VV2V , VV3V , VV4V , VV5V); 
input VV2V , VV3V , VV4V;
output VV5V;
wire WW4W0W;

and f0 (WW4W0W , VV2V , VV3V);
or f1 (VV5V , WW4W0W , VV4V);
endmodule