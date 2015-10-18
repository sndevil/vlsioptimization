module F303 (a , c , VV303V); 
input a , c;
output VV303V;
xor f0 (VV303V , a , c);
endmodule