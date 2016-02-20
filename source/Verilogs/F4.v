module F4 (VV2V , p , v , VV3V , VV4V); 
input VV2V , p , v , VV3V;
output VV4V;
wire WW3W0W , WW3W1W;

or f0 (WW3W0W , VV2V , p);
or f1 (WW3W1W , WW3W0W , v);
and f2 (VV4V , WW3W1W , VV3V);
endmodule