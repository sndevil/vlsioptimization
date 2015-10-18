module F127 (VV63V , VV126V , VV127V); 
input VV63V , VV126V;
output VV127V;
xor f0 (VV127V , VV63V , VV126V);
endmodule