def dispatch(self, request, *args, **kwargs):
    obj = self.get_object()
    if obj.user != self.request.user:
        raise Http404("You are not allowed to edit this Post")
    return super(EditPost, self).dispatch(request, *args, **kwargs)     


    """
  def pre_save(self, obj):
    obj.owner = self.request.user

    """

     """
      if self.action == 'create':
          permission_classes = [IsAdminOrAnonymousUser]
      elif self.action == 'list':
          permission_classes = [IsAdminOrAnonymousUser]
"""