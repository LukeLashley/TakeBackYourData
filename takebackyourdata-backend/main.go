package main

import (
	"io"
	"log"
	"net/http"
)

func main() {
	facebookHandler := func(w http.ResponseWriter, req *http.Request) {
		io.WriteString(w, "TODO: Facebook Handler...")
	}

	http.HandleFunc("/facebook", facebookHandler)
	log.Println("Listing for requests at http://localhost:8000")
	log.Fatal(http.ListenAndServe(":8000", nil))

}
