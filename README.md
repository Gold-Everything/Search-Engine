# Search-Engine
## RPI Content Search Engine
### Large Scale Programming & Testing 2019

#### Architecture

Backend: Django
Frontend: React

#### Design

Send raw(?) query to ranking team API, get list of document ids ranked by relevance. Send that off to document data store to get actual documents. Generate a blurb for each document, display score (maybe), generate a results view. (Basic idea is the goal for now)

#### Contributing

Pull requests are open. Hopefully travis will check whether it conforms to certain stuff.