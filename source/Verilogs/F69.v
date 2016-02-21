module F69 (b , a , VV69V); 
input b , a;
output VV69V;
wire WW68W0W , WW68W1W;

not f0 (WW68W0W , b);
not f1 (WW68W1W , a);
xor f2 (VV69V , WW68W0W , WW68W1W);
endmodule