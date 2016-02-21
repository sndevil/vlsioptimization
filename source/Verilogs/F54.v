module F54 (c , a , VV54V); 
input c , a;
output VV54V;
wire WW53W0W , WW53W1W;

not f0 (WW53W0W , c);
not f1 (WW53W1W , a);
or f2 (VV54V , WW53W0W , WW53W1W);
endmodule