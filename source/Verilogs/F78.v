module F78 (VV70V , VV77V , VV78V); 
input VV70V , VV77V;
output VV78V;
xor f0 (VV78V , VV70V , VV77V);
endmodule