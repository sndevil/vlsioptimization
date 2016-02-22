module F50 (a , d , VV50V); 
input a , d;
output VV50V;
xor f0 (VV50V , a , d);
endmodule