# `sample_crud` (demo only)

This Django app exists for learning CRUD with Django REST Framework. It is **not** part of your eventual production domain.

**Remove when building the real product:**

1. Delete the `sample_crud` package from this repo.
2. Remove `'sample_crud'` from `INSTALLED_APPS` in `config/settings.py`.
3. Remove `path('api/sample/', include('sample_crud.urls'))` from `config/urls.py`.
4. Delete the matching frontend module `React-Frontend/src/sample/` and its import in `App.tsx`.
