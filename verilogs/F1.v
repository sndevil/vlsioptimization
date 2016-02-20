module F1 (a , t , c , VV1V); 
input a , t , c;
output VV1V;
wire WW0W0W;

and f0 (WW0W0W , a , t);
xor f1 (VV1V , WW0W0W , c);
endmodule