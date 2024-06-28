
# rename this file extension to py before executing or after cheking settings

INSTALLED_APPS = [
    # other apps
    'rest_framework',
    'inventory',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
}
