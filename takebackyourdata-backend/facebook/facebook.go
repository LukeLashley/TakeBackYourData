//Package facebook provides a holder for the facebook implementation
package facebook

import (
	"fmt"
	"log"
)

type facebookData struct {
	ads facebookAds
}

//facebookAds struct holds all information relating to ad data on facebook
type facebookAds struct {
	numberOfAdvertisersContacts int
	advertisersContactList      []string
}

// When you want a function to be visible to other classes, it does not follow camelcase
func CreateData() *facebookData {
	fmt.Println("test")
	log.Println("test 2")

	return &facebookData{}
}

// Reads through advertisers_who_uploaded_a_contact_list_with_your_information.json
// Sets numberOfAdvertisersContacts, advertisersContactList in the facebookAds struct
func readAdvertisersContactList() {

}
