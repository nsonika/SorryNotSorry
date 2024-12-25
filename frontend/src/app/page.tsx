import { Laugh } from 'lucide-react';
import ExcuseGenerator from './components/ExcuseGenerator';

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-50 via-purple-50 to-pink-50">
      <div className="container mx-auto px-4 py-12">
        <div className="text-center mb-12">
          <div className="flex items-center justify-center gap-3 mb-4">
            <Laugh className="w-12 h-12 text-indigo-600" />
            <h1 className="text-4xl font-bold text-gray-900">SorryNotSorry</h1>
          </div>
          <p className="text-xl text-gray-600">Your AI-powered excuse generator for life&apos;s awkward moments</p>
        </div>

        <ExcuseGenerator />

        <footer className="mt-16 text-center text-gray-500">
          <p>Need an excuse? We&apos;ve got you covered! 😉</p>
        </footer>
      </div>
    </div>
  );
}
