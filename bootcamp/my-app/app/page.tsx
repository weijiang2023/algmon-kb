/*
import Image from "next/image";
import scene from "@/public/images/scene.png";

export default async function Home() {
  return (
    <main className="relative h-screen">
      <Image 
        src="https://bit.ly/react-cover" 
        alt="cover"
        fill
        className="object-cover"
        sizes="100vw"
        quality={100}
        priority/>
    </main>
  )
}
*/

import Link from 'next/link'
import Image from 'next/image'
import ProductCard from './components/ProductCard'
import { getServerSession } from 'next-auth'
import { authOptions } from './api/auth/[...nextauth]/route'

export default async function Home() {
  const session = await getServerSession(authOptions);

  return (
    <main>
      <h1>Hello { session && <span>{session.user!.name}</span>}</h1>
      <Link href="/users">Users</Link>
      <ProductCard />
    </main>
  )
}
