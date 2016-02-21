module F47 (a , b , VV47V); 
input a , b;
output VV47V;
wire WW46W0W;

not f0 (WW46W0W , a);
xor f1 (VV47V , b , WW46W0W);
endmodule