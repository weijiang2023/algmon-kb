import React, { CSSProperties } from 'react'
import { Html, Body, Container, Tailwind, Text, Link, Preview } from '@react-email/components'

const WelcomeTemplete = ({ name }: { name: string }) => {
  return (
    <Html>
        <Preview>Welcome aboard!</Preview>
        <Tailwind>
            <Body className='bg-white'>
                <Container>
                    <Text className="font-bold text-3xl">Hello {name}</Text>
                    <Link href="https://www.algmon.com">www.algmon.com</Link>
                </Container>
            </Body>
        </Tailwind>

    </Html>
  );
};

const body: CSSProperties = {
    background: '#fff'
}

const heading: CSSProperties = {
    fontSize: '32px'
}

export default WelcomeTemplete