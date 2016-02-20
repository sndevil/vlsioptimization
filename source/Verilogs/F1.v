module F1 (a , b , c , VV1V); 
input a , b , c;
output VV1V;
wire WW0W0W;

or f0 (WW0W0W , a , b);
and f1 (VV1V , WW0W0W , c);
endmodule