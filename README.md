# BlogApiService
A simple blog API service with GraphQl Endpoints using Graphene-Django

## Tech Stacks Used:
* [Python](https://developers.google.com/edu/python/)
* [Django](https://docs.djangoproject.com/en/3.0/intro/install/)
* [GraphQL](https://www.edx.org/course/exploring-graphql-a-query-language-for-apis)
* [Graphene](https://docs.graphene-python.org/projects/django/en/latest/tutorial-plain/)

## Tasks:
1. Implement a `createPost()` mutation which will create a `Post` (a blogpost object) with attributes {`title`, `description`, `publish_date`, `author` (just a name as TextField)}
1. Implement a `updatePost($id)` mutation which will update a `Post` attributes by `$id`
1. Implement a `createComment()` mutation which will create a `Comment` object with attributes {`post` (the blogpost object), `text`, `author` (just the name as a TextField)}
1. Implement a `deleteComment($id)` mutation to delete the given `Comment` by its ID.
1. Implement a `posts()` query to list all the posts
1. Implement a `post($id)` query to get details of a post and all its comments

### Database used:
SQlite DB

## Sample GraphQL codes
```
#Create Post
mutation createMutation {
  createPost(postData: {title: "Graphene Basics", description: "About Graphene", publishDate: "2021-11-15", author: "Bala Vasudevan"}) {
    posts{
      title,
      description,
      publishDate,
      author
    }
  }
}

#Update Post
mutation updateMutation {
  updatePost(postData: {id: 4, title: "Django Basics", description: "About Django Framework", publishDate: "2021-11-15", author: "Sabari"}) {
    posts {
      title,
      description,
      publishDate,
      author
    }
  }
}

#Add a new comment
mutation add_comment{
  addComment(postCommentData: {postIdMapping: 4, author: "SabariNathan005", comment: "Good One bro"}) {
    postComments{
      author
      comment
      createdAt
    }
  }
}

#Delete a comment using ID
mutation delete_comment{
  deleteComment(id: 8) {
    comments {
      author
      comment
    } 
  }
}

#View all posts with the comments
query{
  allPosts{
    id
    title
    description
    publishDate
    author
    commentSet{
      id
      author
      comment
      createdAt
    }
  }
}

#View a specific post with postId
query {
  post(postId: 4) {
    id
    title
    description
    publishDate
    author
    commentSet{
      id
      author
      comment
      createdAt
    }
  }
}

#Delete an existing post with comments using post ID
mutation deleteMutation{
  deletePost(id: 3) {
    posts {
      id
    } 
  }
}

```
