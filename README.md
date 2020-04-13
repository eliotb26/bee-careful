![BeeCareful](https://imgur.com/a/VYjHt3A) @ https://eliotb26.github.io/bee-careful/

## Inspiration

Everyone uses the Internet. Data privacy is a big deal. The GDPR's for Europe, what about the rest of the world?

**Enter _BeeCareful_: Simple crowdsourced details about what websites are using your data for what. Non-for-profit model? Check. Cryptographically secure? Check. Open for contributors? Check.**

_Bees are everywhere. Your data should not be. **BeeCareful lets you Be Carefree!**_

## What it does

BeeCareful is a website that provides crowdsourced information (_by the people, for the people_). It puts data privacy information in the hands of users, who can let others know what they know when it comes to how sites use your data. 

It creates a central place for the common person to understand what is being done with their information. BeeCareful.org will create a site where it will even the grounds between large corporations and the users. Within this site, users are able to create posts about the data that websites store and share. People that post will be required to submit sources with their information but they also have the ability to gain credibility with their amount of posts and the information with which they gathered. 

**The final product of BeeCareful.org represents a platform for learning. It evens the grounds in a subject where many people do not know enough information about. This will lead to more restrictions in data that is retrieved as well as greater knowledge to users about their true privacy.**

## How we built it

With a Python backend, using Flask. Frontend done with simple HTML, CSS & Jinja. XML for database, to store sites' data. hashlib for cryptography. 

## Challenges we ran into

Storing user info while still being the pro-privacy website ourselves. **See below for our solution!**

## Accomplishments that we're proud of

**CRYPTOGRAPHICALLY STORING EMAIL ADDRESSES, NEVER RAW**

Being pro-privacy ourselves, we have to store minimal user data. Yet we need to maintain the integrity of our submissions, and therefore need to register user accounts. 

**So we decided: We'll cryptographically store email addresses, never the raw data.** When you register with us, you provide your email address, which we then hash using SHA-512, which reduces the chance of collisions to nearly insignificantly low. You sign in with your email address, but it's only stored for the few seconds while being hashed. It never goes to disk storage. 

## What we learned

## What's next for BeeCareful

Many big milestones are up ahead, we're just getting started:

* Hosting to our newly-created domain beecareful.org and opening it to the public
* Credential verification so we can better trust users's submissions
* Browser extensions so BeeCareful can instantly give you information when you give data to a website. This will create greater accessibility for the useof this. 
