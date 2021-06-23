# TakeBackYourData

Take back your Data is a React website that is meant to give you a better understanding of what kind of data companies have on you. While also giving you interesting statistics.

## Installation

Install [Go](https://golang.org/dl/)

## Usage

To start the Go back-end:

```bash
cd takebackyourdata-backend
go run main.go
```

To start React front-end

```bash
cd takebackyourdata-web
npm start
```

## Compatability

These companies have an extreme amount of data on you. We could only build functionality for some basic data. See the tables below and if you feel up to the challenge, please create a PR for a functionality.\
[Facebook](###Facebook)\


### Facebook

| Folder                            | File                                                               | Supported | Plan to Support | No plans |
| --------------------------------- | ------------------------------------------------------------------ | --------- | --------------- | -------- |
| activity_messages                 | group_interactions.json                                            |           |                 |          |
| activity_messages                 | people_and_friends.json                                            |           |                 |          |
| ads_information                   | advertisers_who_uploaded_a_contact_list_with_your_information.json |           | X               |          |
| ads_information                   | advertisers_you've_interacted_with.json                            |           | X               |          |
| apps_and_websites_off_of_facebook | apps_and_websites.json                                             |           | X               |          |
| apps_and_websites_off_of_facebook | posts_from_apps_and_websites.json                                  |           | X               |          |
| apps_and_websites_off_of_facebook | your_off-facebook_activity.json                                    |           | X               |          |
| bug_bounty                        | no-data.txt                                                        |           |                 | X        |
| campus                            | no-data.txt                                                        |           |                 | X        |
| comments_and_reactions            | comments.json                                                      |           |                 |          |
| comments_and_reactions            | posts_and_comments.json                                            |           |                 |          |
| events                            | event_invitations.json                                             |           |                 |          |
| events                            | your_event_responses.json                                          |           |                 |          |
| facebook_accounts_center          | accounts_center.json                                               |           |                 |          |
| facebook_gaming                   | no-data.txt                                                        |           |                 | X        |
| facebook_marketplace              | no-data.txt                                                        |           |                 | X        |
| facebook_payments                 | payment_history.json                                               |           |                 |          |
| friends_and_followers             | friends.json                                                       |           |                 |          |
| friends_and_followers             | friend_requests_received.json                                      |           |                 |          |
| friends_and_followers             | friend_requests_sent.json                                          |           |                 |          |
| friends_and_followers             | rejected_friend_requests.json                                      |           |                 |          |
| friends_and_followers             | removed_friends.json                                               |           |                 |          |
| friends_and_followers             | who_you_follow.json                                                |           |                 |          |
| fundraisers                       | no-data.txt                                                        |           |                 | X        |
| groups                            | your_group_membership_activity.json                                |           |                 |          |
| groups                            | your_posts_and_comments_in_groups.json                             |           |                 |          |
| journalist_registration           | no-data.txt                                                        |           |                 | X        |
| location                          | device_location.json                                               |           |                 |          |
| location                          | primary_location.json                                              |           |                 |          |
| location                          | primary_public_location.json                                       |           |                 |          |
| location                          | timezone.json                                                      |           |                 |          |
| music_recommendations             | no-data.txt                                                        |           |                 | X        |
| news                              | your_locations.json                                                |           |                 |          |
| notifications                     | notifications.json                                                 |           |                 |          |
| other_activity                    | pokes.json                                                         |           |                 |          |
| other_logged_information          | ads_interests.json                                                 |           | X               |          |
| other_logged_information          | friend_peer_group.json                                             |           |                 |          |
| other_personal_information        | your_address_books.json                                            |           | X               |          |
| pages                             | pages_you've_liked.json                                            |           |                 |          |
| pages                             | pages_you've_recommended.json                                      |           |                 |          |
| pages                             | pages_you've_unfollowed.json                                       |           |                 |          |
| people_and_friends                | no-data.txt                                                        |           |                 | X        |
| photos_and_videos                 |                                                                    |           |                 | X        |
| polls                             | no-data.txt                                                        |           |                 | X        |
| posts                             | your_pinned_posts.json                                             |           |                 |          |
| posts                             | your_posts_1.json                                                  |           |                 |          |
| preferences                       | language_and_locale.json                                           |           |                 |          |
| privacy_checkup                   | no-data.txt                                                        |           |                 | X        |
| profile_information               | profile_information.json                                           |           |                 |          |
| profile_information               | profile_update_history.json                                        |           |                 |          |
| saved_items_and_collections       | saved_items_and_collections.json                                   |           |                 |          |
| search                            | your_search_history.json                                           |           |                 |          |
| security_and_login_information    | account_activity.json                                              |           |                 |          |
| security_and_login_information    | authorized_logins.json                                             |           |                 |          |
| security_and_login_information    | browser_cookies.json                                               |           |                 |          |
| security_and_login_information    | email_address_verifications.json                                   |           |                 |          |
| security_and_login_information    | ip_address_activity.json                                           |           |                 |          |
| security_and_login_information    | logins_and_logouts.json                                            |           |                 |          |
| security_and_login_information    | login_protection_data.json                                         |           |                 |          |
| security_and_login_information    | mobile_devices.json                                                |           |                 |          |
| security_and_login_information    | record_details.json                                                |           |                 |          |
| security_and_login_information    | where_you're_logged_in.json                                        |           |                 |          |
| security_and_login_information    | your_facebook_activity_history.json                                |           |                 |          |
| short_videos                      | no-data.txt                                                        |           |                 | X        |
| stories                           | no-data.txt                                                        |           |                 | X        |
| voting_location_and_reminders     | location.json                                                      |           |                 |          |
| voting_location_and_reminders     | voting_reminders.json                                              |           |                 |          |
| your_interactions_on_facebook     | recently_viewed.json                                               |           |                 |          |
| your_interactions_on_facebook     | recently_visited.json                                              |           |                 |          |
| your_places                       | places_you've_created.json                                         |           |                 |          |
| your_problem_reports              | no-data.txt                                                        |           |                 | X        |
| your_topics                       | your_topics.json                                                   |           | X               |          |


## Contributors

[Luke Lashley](https://github.com/LukeLashley)\
[Jake Cullom](https://github.com/jpcullom)
