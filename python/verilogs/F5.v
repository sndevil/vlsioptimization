module F5 (VV4V , VV3V , VV5V); 
input VV4V , VV3V;
output VV5V;
wire WW4W0W;

not f0 (WW4W0W , VV4V);
and f1 (VV5V , VV3V , WW4W0W);
endmodule