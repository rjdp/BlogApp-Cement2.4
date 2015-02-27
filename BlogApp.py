#!/usr/bin/env python3

from cement.core.foundation import CementApp
from cement.core.controller import CementBaseController, expose
from cement.core import handler
from pprint import pprint as pp
from rmodel import *
from peewee import *

# define application controllers


class BlogAppBaseController(CementBaseController):

    class Meta:
        label = 'base'
        description = "BlogApp is primitive blog control CLI app ."
        # arguments = [
        #(['--base-opt'], dict(help="option under base controller")),
        # ]

    @expose(help="base controller default command", hide=True)
    def default(self):
        info_msg = "BlogApp - a basic blog control tool."
        banner = '#' + '@' * (len(info_msg) - 2) + '#'
        border = '|' + ' ' * (len(info_msg) - 2) + '|'
        lines = [banner, border, info_msg, border, banner]
        disp = '\n'.join(lines)
        print(disp)
        self.app.args.parse_args(['--help'])


class PostController(CementBaseController):

    class Meta:
        label = 'post'
        stacked_on = 'base'
        stacked_type = 'nested'
        description = "follows Post manipulation subcommands"

    @expose(help="second-controller default command", hide=True)
    def default(self):
        self.app.args.parse_args(['--help'])


class CategoryController(CementBaseController):

    class Meta:
        label = 'category'
        stacked_on = 'base'
        stacked_type = 'nested'
        description = "follows Category manipulation subcommands"

    @expose(help="second-controller default command", hide=True)
    def default(self):
        self.app.args.parse_args(['--help'])


class PostSubController(CementBaseController):

    class Meta:
        label = 'post_sub_controller'
        stacked_on = 'post'
        stacked_type = 'embedded'
        description = "this controller is embedded in the Post Controller"
        arguments = [
            (['extra_arguments'],
             dict(help='title and content', action='store', nargs='*')), (['--category'],
                                                                          dict(help='category name', action='store')),
        ]

    @expose(help="this is a command under the PostController")
    def add(self):
        # self.app.args.parse_args(['--help'])
        if self.app.pargs.extra_arguments and len(self.app.pargs.extra_arguments) == 2:
            title = self.app.pargs.extra_arguments[0]
            content = self.app.pargs.extra_arguments[1]
            if self.app.pargs.category:
                category = self.app.pargs.category
                boo = False
                for p in Category.select():
                    if p.category == category:
                        boo = True
                        break
                if boo == False:
                    cate = Category(category=category)
                    cate.save()
                firstpost = Blog_post(
                    title=title, content=content, category=category)
                firstpost.save()
            else:
                firstpost = Blog_post(title=title, content=content)
                firstpost.save()

    @expose(help="this is a command under the PostController")
    def list(self):
        for p in Blog_post.select():
            print(p.id, p.title, p.content, p.category)

    @expose(help="this is a command under the PostController")
    def search(self):
        if self.app.pargs.extra_arguments and len(self.app.pargs.extra_arguments) == 1 and not(self.app.pargs.category):
            keyword = self.app.pargs.extra_arguments[0]
            for p in Blog_post.select():
                try:
                    if (keyword in p.title) or (keyword in p.content) or (keyword in p.category):
                        print(p.id, p.title, p.content, p.category)
                except:
                    pass


class CategorySubController(CementBaseController):

    class Meta:
        label = 'category_sub_controller'
        stacked_on = 'category'
        stacked_type = 'embedded'
        description = "this controller is embedded the Category Controller"
        arguments = [
            (['xtra_arguments'],
             dict(help='<category-name> or {<post-id> and <cat-id>}', action='store', nargs='*')),
        ]

    @expose(help="this is a command under the CategoryController")
    def add(self):
        if self.app.pargs.xtra_arguments and len(self.app.pargs.xtra_arguments) == 1:
            cat_name = self.app.pargs.xtra_arguments[0]
            cat = Category(category=cat_name)
            cat.save()

    @expose(help="this is a command under the CategoryController")
    def list(self):
        for p in Category.select():
            print(p.id, p.category)

    @expose(help="this is a command under the CategoryController")
    def assign(self):
        if self.app.pargs.xtra_arguments and len(self.app.pargs.xtra_arguments) == 2:
            post_id = int(self.app.pargs.xtra_arguments[0])
            cat_id = int(self.app.pargs.xtra_arguments[1])
            boo = False
            for c in Category.select():
                print(type(c.id), type(cat_id))
                if c.id == cat_id:
                    boo = True
                    cat = c.category
                    break
            if boo == False:
                print("mentioned category id doesnt exist")
            else:
                foo = False
                for b in Blog_post.select():
                    if b.id == post_id:
                        foo = True
                        b.category = cat
                        b.save()
                        break
                if foo == False:
                    print("mentioned post id doesnt exist")


def main():
    try:
        # create the application
        app = CementApp('BlogApp')

        # register controllers
        handler.register(BlogAppBaseController)
        handler.register(PostController)
        handler.register(CategoryController)
        handler.register(PostSubController)
        handler.register(CategorySubController)
        # setup the application
        app.setup()

        # run the application
        app.run()
    finally:
        # close the application
        app.close()

if __name__ == '__main__':
    main()
