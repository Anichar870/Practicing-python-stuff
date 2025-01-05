package main

import (
	"fmt"
	"net/http"
)

func main() {
	// Define a handler function for the root URL
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintln(w, "Hello, World!")
	})

	// Define the port to listen on
	port := "8080"
	fmt.Printf("Server is running on http://localhost:%s\n", port)

	// Start the server
	if err := http.ListenAndServe(":"+port, nil); err != nil {
		fmt.Println("Error starting server:", err)
	}
}
