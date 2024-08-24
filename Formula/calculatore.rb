class Calculatore < Formula
  desc "A simple command-line (Italian) calculator"
  homepage "https://github.com/doribenba/calculatore.git"
  url "https://github.com/doribenba/calculatore/releases/download/v2/calculatore-1.0.1.tar.gz"
  sha256 "82e8455530ab908438f378d5e77817c68c449451bbb0a6619337c2115e4ee77a"

  def install
    bin.install "calculatore" 
  end

  test do
    system "#{bin}/calculatore", "--help"
  end
end
