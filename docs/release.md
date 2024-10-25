# Releases

!!! info "Changelog"

    This document describes how we release uMap.

    If you are looking for the releases changelog, [please go there](changelog.md).


## How to make a release

1. Make sure JS packages are up to date:
    - `make installjs vendors`
1. Run tests:
    - `make test`
1. I18N
    - `make messages` look for new strings within the code
    - `make tx_push` to publish new strings [to transifex](https://app.transifex.com/openstreetmap/umap/dashboard/)
    - translators at work
    - `make tx_pull` to retrieve new translations from transifex
    - `make compilemessages` to create regular `.mo` + `umap/static/umap/locale/*.js`
    - commit new translations `git commit -am "i18n"`
2. Test collectstatic: `umap collectstatic --no-input`
2. Bump version: `make patch|minor`
2. Ask automatic release notes to Github: `make changelog` and paste it in `docs/changelog.md`
3. `git commit -am "2.X.Y"`
4. `git tag 2.X.Y`
5. `git push && git push --tag`
6. Go to [Github release page](https://github.com/umap-project/umap/releases/new) and paste release notes
7. `make build`
8. `make publish`
9. `make docker`

### Deploying instances

#### OSMfr

We use a custom flat Makefile, versioned [here](https://github.com/umap-project/umap-deploy).

To deploy a new version on the [dev](https://dev.umap-project.org) server:

- edit the `.env.dev` file and change the version number
- run this command `FLAVOUR=dev make deploy`

To deploy a new version on OSM France servers:

- edit the `.env.osmfr` file and change the version number
- run this command `FLAVOUR=osmfr make deploy`

#### ANCT

Update the [Dockerfile](https://gitlab.com/incubateur-territoires/startups/donnees-et-territoires/umap-dsfr-moncomptepro/-/blob/main/Dockerfile?ref_type=heads) with correct version and put a tag `YYYY.MM.DD` in order to deploy it to production.


## When to make a release

We aim to support [Baseline](https://developer.mozilla.org/en-US/blog/baseline-evolution-on-mdn/) “Widely available” (implemented in major browsers within the last 30 months).

### Major (2.Y.Z)

* when we bump Django to a major version
* when we change how we store data (both in database and filesystem)
* when we change the deployment system requirements

### Minor (X.3.Z)

* when we add new features
* when we improve an existing feature
* when we improve the usability
* when we change templates

If it's not a major nor a patch, it's a minor.

### Patch (X.Y.12)

* when there are bugfixes
