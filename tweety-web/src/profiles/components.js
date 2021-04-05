import React from 'react' 


/// HANDLES THE USERNAME LINK ON TWEET DISPLAY
export function UserLink(props) {
  const {username} = props 
  const handleUserLink = (event) => {
      window.location.href=`/profiles/${username}`
  }
  return <span className='pointer' onClick={handleUserLink}> 
    {props.children}
  </span>
}

/// HANDLES THE OVERALL USER DISPLAY ON A TWEET
export function UserDisplay(props) {
    const {user, includeFullName} = props 

    if(user === undefined) {
      return <div>Loading... </div> 
    }

    const nameDisplay = includeFullName === true ? `${user.first_name} ${user.last_name} ` : null
    

    return <React.Fragment> 
      {nameDisplay}
      <UserLink username={user.username}> @{user.username} </UserLink> 
    </React.Fragment>
  }

/// HANDLES THE USER PICTURE AND LINKS IT TO USER PROFILE ON TWEET DISPLAY
export function UserPicture(props) {
  const {user} = props

  if(user === undefined) {
    return <div>Loading... </div> 
  }

  return <UserLink username={user.username}><span className= 'mx-1 px-3 py-2 rounded-circle bg-dark text-white'> 
    {user.username[0]}
  </span> </UserLink>
}


