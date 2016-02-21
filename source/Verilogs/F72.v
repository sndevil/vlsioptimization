module F72 (a , d , VV72V); 
input a , d;
output VV72V;
wire WW71W0W , WW71W1W;

not f0 (WW71W0W , a);
not f1 (WW71W1W , d);
and f2 (VV72V , WW71W0W , WW71W1W);
endmodule