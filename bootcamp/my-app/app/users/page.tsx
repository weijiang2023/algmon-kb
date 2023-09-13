import Link from 'next/link'
import React from 'react'
import UserTable from './UserTable'

interface Props {
    searchParams: { sortOrder: string}    
}

const UsersPage = async ({ searchParams: { sortOrder } }: Props) => {
    console.log(sortOrder)

    return (
        <>
            <h1>Users</h1>
            <Link href="/users/new" className='btn'>New User</Link>
            <UserTable sortOrder={sortOrder}/>
        </>
    )
}

export default UsersPage