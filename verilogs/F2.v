module F2 (d , a , VV2V); 
input d , a;
output VV2V;
wire WW1W0W;

not f0 (WW1W0W , d);
or f1 (VV2V , WW1W0W , a);
endmodule