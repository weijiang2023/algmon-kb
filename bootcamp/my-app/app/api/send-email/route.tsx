import WelcomeTemplete from "@/emails/WelcomeTemplete";
import { NextResponse } from "next/server";
import { Resend } from "resend";

const resend = new Resend(process.env.RESEND_API_KEY);

export async function POST() {
    resend.emails.send({
        from: '...',
        to: 'weijiang2009@gmail.com',
        subject: '...',
        react: <WelcomeTemplete name="Wei" />
    })

    return NextResponse.json( {} );
}