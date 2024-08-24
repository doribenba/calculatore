class Calculatore < Formula
  desc "A simple command-line (Italian) calculator"
  homepage "https://github.com/doribenba/calculatore.git"
  url "https://github.com/doribenba/calculatore/releases/download/v2/calculatore-1.0.1.tar.gz"
  sha256 "a81001aff3f62ef5d7a61ae4752cfb1e7bef9c7c2f4e138af9060cded373c370"

  def install
    bin.install "calculatore" 
  end

  test do
    system "#{bin}/calculatore", "--help"
  end
end
